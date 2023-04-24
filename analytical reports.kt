// Define the data model for your analytical reports
@Entity(tableName = "reports")
data class Report(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val name: String,
    val data: String
)

// Define the Room database
@Database(entities = [Report::class], version = 1)
abstract class ReportDatabase : RoomDatabase() {
    abstract fun reportDao(): ReportDao

    companion object {
        @Volatile
        private var INSTANCE: ReportDatabase? = null

        fun getInstance(context: Context): ReportDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    ReportDatabase::class.java,
                    "report_database"
                ).build()
                INSTANCE = instance
                instance
            }
        }
    }
}

// Define the DAO for accessing reports
@Dao
interface ReportDao {
    @Query("SELECT * FROM reports")
    fun getAll(): List<Report>

    @Insert
    fun insert(report: Report)

    @Delete
    fun delete(report: Report)
}
// Insert a new report into the database
val report = Report(name = "Sales Report", data = "...")
ReportDatabase.getInstance(context).reportDao().insert(report)

// Retrieve all reports from the database
val reports = ReportDatabase.getInstance(context).reportDao().getAll()
