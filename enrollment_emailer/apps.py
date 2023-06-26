from django.apps import AppConfig

class EnrollmentEmailerConfig(AppConfig):
    name = 'enrollment_emailer'
    verbose_name = "Enrollment Emailer"

    def ready(self):
        # import signal handlers
        import enrollment_emailer.signals
