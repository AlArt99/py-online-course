class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days / 7
        return int(weeks) + (weeks > int(weeks))

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict.get("days", 0))
        )
