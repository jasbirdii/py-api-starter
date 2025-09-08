import logging
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

logger = logging.getLogger(__name__)


class TaskScheduler:
    """Background task scheduler using APScheduler."""

    def __init__(self):
        self.scheduler: AsyncIOScheduler | None = None

    def start(self):
        """Start the scheduler."""
        if self.scheduler and self.scheduler.running:
            return

        self.scheduler = AsyncIOScheduler()
        self._register_jobs()
        self.scheduler.start()
        logger.info("Task scheduler started")

    def stop(self):
        """Stop the scheduler."""
        if self.scheduler and self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("Task scheduler stopped")

    def _register_jobs(self):
        """Register all background jobs."""
        if not self.scheduler:
            return

        # Example: Run every 5 minutes
        self.scheduler.add_job(
            self.cleanup_old_data,
            trigger=IntervalTrigger(minutes=5),
            id="cleanup_old_data",
            name="Cleanup old data",
            replace_existing=True
        )

        # Example: Run daily at midnight
        self.scheduler.add_job(
            self.daily_report,
            trigger=CronTrigger(hour=0, minute=0),
            id="daily_report",
            name="Daily report",
            replace_existing=True
        )

        # Example: Run every hour
        self.scheduler.add_job(
            self.health_check,
            trigger=IntervalTrigger(hours=1),
            id="health_check",
            name="Health check",
            replace_existing=True
        )

    async def cleanup_old_data(self):
        """Cleanup old data job."""
        logger.info(f"Running cleanup job at {datetime.utcnow()}")
        # Add your cleanup logic here
        # Example: Delete old logs, expired sessions, etc.
        pass

    async def daily_report(self):
        """Daily report job."""
        logger.info(f"Running daily report at {datetime.utcnow()}")
        # Add your daily report logic here
        # Example: Generate usage statistics, send reports, etc.
        pass

    async def health_check(self):
        """Health check job."""
        logger.info(f"Running health check at {datetime.utcnow()}")
        # Add your health check logic here
        # Example: Check external services, database connectivity, etc.
        pass


# Global scheduler instance
scheduler = TaskScheduler()


def register_jobs(app):
    """Register background jobs with the FastAPI app."""
    @app.on_event("startup")
    async def startup_event():
        scheduler.start()

    @app.on_event("shutdown")
    async def shutdown_event():
        scheduler.stop()
