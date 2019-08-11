import pwd

def user_names():
    return [ user.pw_name for user in pwd.getpwall()
<<<<<<< HEAD
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]
=======
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]
>>>>>>> 7948095d8bc8122ef2ba4db36af91f2f7bb294b3
