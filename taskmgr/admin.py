from django.contrib import admin
from django.contrib import admin
from .models import Employee, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'employee', 'status', 'due_date', 'days_left')
    search_fields = ('title',)
    list_filter = ('status',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'joining_date')
    inlines = [TaskInline]

# Register your models here.
