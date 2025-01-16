from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password")
        # Create a test task
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            completed=False,
            user=self.user
        )

    def test_task_creation(self):
        """Test if the task is created successfully and attributes are correctly assigned."""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.user, self.user)

    def test_task_default_ordering(self):
        """Test if the default ordering of tasks is by 'completed'."""
        task2 = Task.objects.create(
            title="Another Task",
            completed=True,
            user=self.user
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], self.task)  # The first task is not completed
        self.assertEqual(tasks[1], task2)  # The second task is completed

    def test_task_string_representation(self):
        """Test the string representation of the task model."""
        self.assertEqual(str(self.task), "Test Task")

    def test_task_user_null(self):
        """Test behavior when a task has no user assigned."""
        task_without_user = Task.objects.create(
            title="Task Without User",
            description="No user assigned.",
            completed=False
        )
        self.assertIsNone(task_without_user.user)
