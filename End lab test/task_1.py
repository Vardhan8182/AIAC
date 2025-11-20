from dataclasses import dataclass
import unittest

"""
task_1.py

A simple Student class for an AI-assisted attendance app.

Features:
- mark_attendance(present: bool = True, count: int = 1)
- calculate_attendance_percentage(decimals: int = 2) -> float

Includes inline documentation, type hints, and unit tests.
"""



@dataclass
class Student:
    """
    Represents a student and their attendance record.

    Attributes:
        student_id: Optional unique identifier for the student.
        name: Student's name.
        total_classes: Total number of classes recorded for this student.
        attended_classes: Number of classes the student attended.
    """
    student_id: str = ""
    name: str = ""
    total_classes: int = 0
    attended_classes: int = 0

    def mark_attendance(self, present: bool = True, count: int = 1) -> None:
        """
        Mark attendance for one or more class sessions.

        Args:
            present: True if the student attended the session(s), False otherwise.
            count: Number of consecutive sessions to mark (must be >= 1).

        Raises:
            ValueError: If count is not a positive integer.
        """
        if not isinstance(count, int) or count < 1:
            raise ValueError("count must be a positive integer (>= 1)")

        # Increment total classes by count, and attended_classes when present
        self.total_classes += count
        if present:
            self.attended_classes += count

    def calculate_attendance_percentage(self, decimals: int = 2) -> float:
        """
        Calculate the attendance percentage (0-100).

        Args:
            decimals: Number of decimal places to round the result to.

        Returns:
            Attendance percentage as a float rounded to `decimals` places.
            Returns 0.0 if no classes have been recorded yet.
        """
        if self.total_classes == 0:
            return 0.0
        percentage = (self.attended_classes / self.total_classes) * 100.0
        return round(percentage, decimals)

    def __repr__(self) -> str:
        return (
            f"Student(student_id={self.student_id!r}, name={self.name!r}, "
            f"attended_classes={self.attended_classes}, total_classes={self.total_classes})"
        )


# -------------------------
# Unit tests
# -------------------------


class TestStudentAttendance(unittest.TestCase):
    def test_initial_state(self):
        s = Student(student_id="S1", name="Alice")
        self.assertEqual(s.attended_classes, 0)
        self.assertEqual(s.total_classes, 0)
        self.assertEqual(s.calculate_attendance_percentage(), 0.0)

    def test_mark_single_present(self):
        s = Student(name="Bob")
        s.mark_attendance(present=True)
        self.assertEqual(s.total_classes, 1)
        self.assertEqual(s.attended_classes, 1)
        self.assertEqual(s.calculate_attendance_percentage(), 100.0)

    def test_mark_single_absent(self):
        s = Student(name="Cara")
        s.mark_attendance(present=False)
        self.assertEqual(s.total_classes, 1)
        self.assertEqual(s.attended_classes, 0)
        self.assertEqual(s.calculate_attendance_percentage(), 0.0)

    def test_mark_multiple_sessions(self):
        s = Student(name="Dave")
        s.mark_attendance(present=True, count=3)   # attended 3 of 3
        s.mark_attendance(present=False, count=2)  # attended 3 of 5
        self.assertEqual(s.total_classes, 5)
        self.assertEqual(s.attended_classes, 3)
        self.assertEqual(s.calculate_attendance_percentage(), 60.0)

    def test_invalid_count(self):
        s = Student(name="Eve")
        with self.assertRaises(ValueError):
            s.mark_attendance(present=True, count=0)
        with self.assertRaises(ValueError):
            s.mark_attendance(present=True, count=-1)
        with self.assertRaises(ValueError):
            s.mark_attendance(present=True, count=1.5)  # not int

    def test_rounding(self):
        s = Student(name="Frank")
        # 2 attended of 3 total -> 66.666... -> rounded to 2 decimals 66.67
        s.mark_attendance(present=True, count=2)
        s.mark_attendance(present=False, count=1)
        self.assertEqual(s.calculate_attendance_percentage(decimals=2), 66.67)
        # Allow different decimals
        self.assertEqual(s.calculate_attendance_percentage(decimals=1), 66.7)
        self.assertEqual(s.calculate_attendance_percentage(decimals=0), 67.0)

    def test_repr(self):
        s = Student(student_id="X1", name="Gina")
        s.mark_attendance(True, 2)
        s.mark_attendance(False, 1)
        r = repr(s)
        self.assertIn("student_id='X1'", r)
        self.assertIn("name='Gina'", r)
        self.assertIn("attended_classes=2", r)
        self.assertIn("total_classes=3", r)


if __name__ == "__main__":
    unittest.main()