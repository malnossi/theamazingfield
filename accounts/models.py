from django.db import models

class Department(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):

    department = models.ForeignKey(Department,
                                    on_delete=models.CASCADE,
                                    related_name="employees")
    employee_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.employee_name