#   Imports w/ Clear
import shutil
import os
import pickle

os.system("clear")

#   GAM Directory
gam_folder = '/path/to/gam/directory/'

#   Oauth directories
domain1_folder = '/path/to/domain1/oauth/files/'
domain2_folder = '/path/to/domain2/oauth/files/'
domain3_folder = '/path/to/domain3/oauth/files/'
domain4_folder = '/path/to/domain4/oauth/files/'
domain5_folder = '/path/to/domain5/oauth/files/'
domain6_folder = '/path/to/domain6/oauth/files/'

#   Domains
domain1 = 'domain1.com'
domain2 = 'domain2.org'
domain3 = 'domain3.net'
domain4 = 'domain4.edu'
domain5 = 'domain5.gov'
domain6 = 'domain6.info'

#   Opens saved pickle variable 'current_domain'
with open(str(gam_folder) + 'domain.txt', 'rb') as domainpickle:
    current_domain = pickle.load(domainpickle)
#   I turned myself into a pickle, Morty! Boom! Big reveal: I'm a pickle. 

#   Current domain loop
domain_loop = True
while domain_loop:
    print('\nCurrent Domain: '+ current_domain)
    print('[1] Change Domains')
    print('[2] Exit')
    answer = input('\n: ') 
    if answer == '1':
        domain_loop = False
    if answer == '2':
        quit()
if not domain_loop: 
    print('\nSelect a domain:')
    print('[1] ', domain1)
    print('[2] ', domain2)
    print('[3] ', domain3)
    print('[4] ', domain4)
    print('[5] ', domain5)
    print('[6] ', domain6)

#   Copy loop
copy_loop = True
while copy_loop:
    sel = input('\n: ')
#   Selection 1
    if sel == '1':
        if current_domain == domain1:
            print('\nThis is already the current domain')
            quit()
        else:
            current_domain = domain1
            pickle.dump(current_domain, open(str(gam_folder) + 'domain.txt', 'wb'))
            print('\nSwitching domain to: ' + domain1)
            for file_name in os.listdir(domain1_folder):
                source = domain1_folder + file_name
                destination = gam_folder + file_name
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied:', file_name)
                    copy_loop = False
#   Selection 2
    if sel == '2':
        if current_domain == domain2:
            print('\nThis is already the current domain')
            quit()
        else:
            current_domain = domain2
            pickle.dump(current_domain, open(str(gam_folder) + 'domain.txt', 'wb'))
            print('\nSwitching domain to: ' + domain2)
            for file_name in os.listdir(domain2_folder):
                source = domain2_folder + file_name
                destination = gam_folder + file_name
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied:', file_name)
                    copy_loop = False
#   Selection 3
    if sel == '3':
        if current_domain == domain3:
            print('\nThis is already the current domain')
            quit()
        else:
            current_domain = domain3
            pickle.dump(current_domain, open(str(gam_folder) + 'domain.txt', 'wb'))
            print('\nSwitching domain to: ' + domain3)
            for file_name in os.listdir(domain3_folder):
                source = domain3_folder + file_name
                destination = gam_folder + file_name
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied:', file_name)
                    copy_loop = False
#   Selection 4
    if sel == '4':
        if current_domain == domain4:
            print('\nThis is already the current domain')
            quit()
        else:
            current_domain = domain4
            pickle.dump(current_domain, open(str(gam_folder) + 'domain.txt', 'wb'))
            print('\nSwitching domain to: ' + domain4)
            for file_name in os.listdir(domain4_folder):
                source = domain4_folder + file_name
                destination = gam_folder + file_name
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied:', file_name)
                    copy_loop = False
#   Selection 5
    if sel == '5':
        if current_domain == domain5:
            print('\nThis is already the current domain')
            quit()
        else:
            current_domain = domain5
            pickle.dump(current_domain, open(str(gam_folder) + 'domain.txt', 'wb'))
            print('\nSwitching domain to: ' + domain5)
            for file_name in os.listdir(domain5_folder):
                source = domain5_folder + file_name
                destination = gam_folder + file_name
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied:', file_name)
                    copy_loop = False
#   Selection 6
    if sel == '6':
        if current_domain == domain6:
            print('\nThis is already the current domain')
            quit()
        else:
            current_domain = domain6
            pickle.dump(current_domain, open(str(gam_folder) + 'domain.txt', 'wb'))
            print('\nSwitching domain to: ' + domain6)
            for file_name in os.listdir(domain6_folder):
                source = domain6_folder + file_name
                destination = gam_folder + file_name
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied:', file_name)
                    copy_loop = False
#   End copy loop
    if not copy_loop:
        print('\nSwitch complete.\n')
