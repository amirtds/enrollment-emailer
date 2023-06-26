from setuptools import setup, find_packages

setup(
    name='enrollment_emailer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3,<3.3',
    ],
    entry_points={
        'lms.djangoapp': [
            'enrollment_emailer = enrollment_emailer.apps:EnrollmentEmailerConfig',
        ],
    },
)
