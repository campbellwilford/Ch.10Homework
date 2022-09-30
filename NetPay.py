import EmployeeClass as emp
import PayrollDeductionClass as pay

employee = emp.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

charge1 = pay.PayrollDeduction('food court','8/14/2022', 22.50, 39119)
charge2 = pay.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
charge3 = pay.PayrollDeduction('food court','8/17/2022', 15.25, 21547)
charge4 = pay.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
charge5 = pay.PayrollDeduction('vending machine','8/5/2022', 2.75, 58475)

from tabulate import tabulate 
table = [['Name','ID Number','Department','Job Title','Monthly Salary'],[employee.getName(), employee.getID(), employee.getDepartment(),employee.getJob(),employee.getSalary()]]
print(tabulate(table))
print()


print('*** Employee Pay ***')
print('Name:', employee.getName())
print('ID Number', employee.getID())
print('Department:', employee.getDepartment())
print('Gross Pay: $', employee.getSalary(),sep='')
print('Net Pay:$', employee.getSalary() - charge2.getCharge()-charge4.getCharge()-charge5.getCharge(),sep='')

