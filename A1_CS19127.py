### MUHAMMAD SHAFAY AZEEM
### CS-19127
def bonus():
## This function is called when your stock beacomes zero and it calculates  bonus by incrememnt of 10 percent in salary..
    print('Congratulations Our employees have been given bonuses')
    per_hour_wage=65
    for numbers in range(1,3):
        print(f'Enter work hours of employee {numbers} :', end=" ")
        hours=int(input())
        salary=per_hour_wage*hours
        print(f'Salaray for Employee {numbers} for working {hours} hours is {salary} ruppes')
        if total_samosa_stock==0 and total_roll_stock==0:
            increment = salary*(10/100)
            wage=salary+increment
            print (f'Now salary_with_bonus_for_employee {numbers} is {wage} rupees')

def add_stock():
## it''ll help you to refresh your stock incase if you want to refill your bakery you can call tis function
    global total_samosa_stock
    global total_roll_stock
    samosa_increment=int(input('Enter number of samosas: '))
    total_samosa_stock+=samosa_increment
    roll_increment=int(input('Enter number of rolls: '))
    total_roll_stock+=roll_increment
    
def employee_wages():
## This funtion simply gets you salary.
    per_hour_wage=65
    for numbers in range(1,3):
        print(f'Enter work hours of employee {numbers} :', end=" ")
        hours=int(input())
        salary=per_hour_wage*hours
        print(f'Salaray for Employee {numbers} for working {hours} hours is {salary} ruppes')
        
def print_menu():
        print("ITEM        PPRICE")
        menu=[["Samosa", 'Rs-10'],["Roll",'RS-15']]
        for item in menu:
            print(f'{item[0]:12}{item[1]:12}')
        order_bill()
        
def order_bill():
##This Function calcultes your bill.
    global total_samosa_stock,total_roll_stock
    choice=input('Press 1 to order samosa \nPress 2 to order roll \nPress 3 to order roll and samosa both\n')
    if choice=='1':
        samosa=int(input('Sir, how many samosas do you want??'))
        Bill= samosa*10
        print ('Your Bill is=',Bill)
        Lst_samosa.append(samosa)
        total_samosa_stock=total_samosa_stock-(samosa)
    elif choice=='2':
        roll=int(input('Sir, how many roll do you want?'))
        Bill=roll*15
        print ('Your Bill is=',Bill)
        Lst_roll.append(roll)
        total_roll_stock=total_roll_stock-(roll)
    else:
        samosa=int(input('Sir, how many samosas do you want?'))
        roll=int(input('Sir, how many roll do you want?'))
        Bill=(samosa*10 )+(roll*15)
        print ('Your Bill is=',Bill)
        Lst_roll.append(roll)
        Lst_samosa.append(samosa)
        total_samosa_stock=total_samosa_stock-(samosa)
        total_roll_stock=total_roll_stock-(roll)
    items_in_stock()
    
def items_in_stock():
# this function will tell you how much rolls and samosas are left
    global total_samosa_stock,total_roll_stock
    
    if total_samosa_stock>0 and total_roll_stock>0:
        print(f'\nwe have {total_samosa_stock} samosas and {total_roll_stock} rolls')

    elif total_samosa_stock>0 and total_roll_stock==0:
        print(f'\nwe have only {total_samosa_stock} samosas left no roll left')

    elif total_samosa_stock==0 and total_roll_stock>0:
        print(f'\nwe have only {total_roll_stock} rolls left no samosa left')

    else:
        print('\nSorry !! but now we are out of stock')
        
def boutique():
##this Function prints menu and take order and calculate your bill and will give you scheme if your bill exceeds from 10,000 and deduct that amount from main stock
    global total_samosa_stock,total_roll_stock
    print('WELCOME TO OUR BOUTIQUE SHOP')
    print('DRESSES                                           PRIZE')
    menu=[['Designer Lehnga' , 'Rs=50000-90000'],['Kurtis' , 'Rs=1000-6000'],['Pajamas','Rs=800-3000']]
    for item in menu:
        print(f'{item[0]:50}{item[1]:50}')
    choice=input('Press 1 to order designer lehnga \nPress 2 to order kurtis \nPress 3 to order pajamas \n')
    if choice=='1':
        print('Lehnga                        PRIZE')
        lehnga_menu=[['Normal lehnga' ,'Rs-55000'],['Heavy Lehnga', 'Rs-85000']]
        for lehnga in menu:
            print(f'{lehnga[0]:30}{lehnga[1]:30}')
        choice=input('Press 1 to order Normal lehnga \nPress 2 to order Heavy lehnga \n')
        if choice=='1':    
            print('Thankyou for shoppoing sir, your Bill is 50000 rupees')
            print(f'Congratulations sir, you have given 1 dozen samosas and rolls')
            total_samosa_stock-=12
            total_roll_stock-=12
            print(f'Now you have {total_samosa_stock} samosas and {total_roll_stock} rolls left in bakeshop')
        else:
            print('Thankyou for shoppoing sir, your Bill is 85000 rupees')
            print(f'Congratulations sir, you have given 1 dozen samosas and rolls')
            total_samosa_stock-=12
            total_roll_stock-=12
            print(f'Now you have {total_samosa_stock} samosas and {total_roll_stock} rolls left in bakeshop')
    elif choice=='2':
            print('Kurtis                   PRIZE')
            kurti_menu=[['Khaadi Kurti' ,'Rs-6000'],['Sapphire Kurti', 'Rs-5000']]
            for kurti in kurti_menu:
                 print(f'{kurti[0]:25}{kurti[1]:25}')
            choice=input('Press 1 to order Khaadi kurti \nPress 2 to order Sapphire Kurti\n')
            if choice=='1':
                print(f'Thankyou for shoppoing sir, your Bill is 6000 rupees')
                print(f'Congratulations sir, you have given 1 dozen samosas')
                total_samosa_stock-=12
                print(f'Now you have {total_samosa_stock} samosas left in bakeshop')
            else:
                print(f'Thankyou for shoppoing sir, your Bill is 5000 rupees')
                print(f'Congratulations sir, you have given 1 dozen samosas')
                total_samosa_stock-=12
                print(f'Now you have {total_samosa_stock} samosas in bakeshop')
    elif choice=='3':
            print('Pajama                    PRIZE')
            pajama_menu=[['Simple Pajama' ,'Rs-1200'],['Embroidery Pajama', 'Rs-2700']]
            for pajama in pajama_menu:
                print(f'{pajama[0]:25}{pajama[1]:25}')
            choice=input('Press 1 to order Simple Pajama \nPress 2 to order Embroidery Pajama\n')
            if choice=='1':
                print(f'Thankyou for shoppoing sir, your Bill is 1200 rupees')
            else:
                print(f'Thankyou for shoppoing sir, your Bill is 2700 rupees')

Lst_samosa=[]
Lst_roll=[]
total_samosa_stock = 30
total_roll_stock = 30
while True:

     print('''Mr.Shafay has two shops...
              1.BAKESHOP
              2.BOUTIQUE SHOP
              3.ADD STOCK
              4.EXIT 
          Which one do you want to go?''')
     choice=int(input('Enter your answer in 1 or 2 or 3 or 4:'))
## if you press 1 and your total stock is zero it'll calculate your bonus and wage acc to your work hours and if your remaining stock is not zero it'll let you through my bake shop
     
     
     if choice==1:
         if total_roll_stock==0 and total_samosa_stock==0:
             bonus()
         if (total_samosa_stock>0 and total_roll_stock>0) or (total_samosa_stock==0 and total_roll_stock>0) or (total_samosa_stock>0 and total_roll_stock==0):
    
               print('''Which of the following option you want to choose?
                        1.ORDER
                        2.Empolyees wages''')
               choose=int(input('enter you choice ? '))
               if choose==1:
                    print('\nWELCOME TO OUR BAKESHOP')
                    print(f'\nThere are {total_samosa_stock} samosas and {total_roll_stock} rolls in stock')
                    print_menu()
               elif choose==2:
                    if (total_samosa_stock>0 and total_roll_stock>0) or (total_samosa_stock==0 and total_roll_stock>0) or (total_samosa_stock>0 and total_roll_stock==0):
                        employee_wages()
               else:
                    bonus()
     elif choice==2:
          boutique()
     elif choice==3:
         add_stock()
     else:
         break
         
