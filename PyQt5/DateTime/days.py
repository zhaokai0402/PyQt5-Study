from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

d = QDate(1945, 4, 7)

print("Days in month: {0}".format(d.daysInMonth()))
print("Days in year: {0}".format(d.daysInYear()))