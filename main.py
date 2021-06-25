import requests
import mysql.connector
import secrets
from colorama import Fore, Back, Style
mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)
balm = 0
#print(mydb)

#mycursor.execute("CREATE TABLE ID (name VARCHAR(255), BALANCE VARCHAR(255))")
#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
  #print(x)
mycursor = mydb.cursor()
token = secrets.token_hex(nbytes=16)

choice = input(f"{Fore.BLUE}Do you have an account? [Y or N]:")
if choice == "Y":
  print(Fore.GREEN + "Awesome!")
  pass
elif choice == "N":
  print(Fore.GREEN + "Okay cool!")
  sql_q = "INSERT INTO ID (name, balance) VALUES (%s, %s)"
  val = (token, 0)
  mycursor.execute(sql_q,val)
  mydb.commit()
  print(Fore.GREEN , mycursor.rowcount, f"Token created for you and inserted into database called {token}")
else:
  choice = input(f"{Fore.BLUE}Do you have an account? [Y or N]:")


token_user = input(Fore.GREEN + "Enter token:")
token_user_str = str(token_user)




try:
    sql_q = "SELECT * FROM ID"
    token_from_db = mycursor.execute(sql_q)
    result = mycursor.fetchall()
    token_user_striped = token_user.strip()
    tokens = [token for (token, _) in result]
    if token_user in tokens:
      print(Fore.GREEN + "Logged in!")
      logged_in = True

    #if (token_user,) not in result:
    else:
      logged_in = False
      ye_nah = input(f"{Fore.RED}Account Not Found! , Want to make one? [Y or N]:")
      if ye_nah == "Y":
        sql_q = "INSERT INTO ID (name, balance) VALUES (%s, %s)"
        val = (token, 0)
        mycursor.execute(sql_q,val)
        mydb.commit()
        print(Fore.BLUE , f"We have created a new token for you to practice with. This token is {token}")
        print(Fore.BLUE , mycursor.rowcount, f"Token inserted into database called {token}")
        pass
      elif ye_nah == "N":
        exit
      else:
        ye_nah = input(f"{Fore.RED}Account Not Found! , Want to make one? [Y or N]:")

except Exception as e:
    print(e)

try:
  get_balance = f"SELECT balance FROM ID WHERE name=(%s)" #:(((((
  val = (token_user, )
  balance_getting = mycursor.execute(get_balance, val)
  balance = mycursor.fetchall()
  mydb.commit()
  print(Fore.GREEN + "Welcome to DsawCoin!")
  print(Fore.GREEN + "dsawcoin.tk")
  #while logged_in == True:
  while logged_in == True:
    i_suck = input("DsawCoin >")
    #stuff = ["cp","buy","sell","help","about","exit","gen","bal","balm"]
    #done = ["about","help","exit","bal","gen","sell","balm","cp","help"]
    if i_suck == "help":
      print(Fore.GREEN , "Welcome to DsawCoin")
      print(Fore.GREEN , "The crypto of your dreams!")
      print(Fore.GREEN , "Use command - cp to get the DsawCoin's curent price!")
      #print(Fore.GREEN , "Use command - bp to get the DsawCoin's old price!")
      print(Fore.GREEN , "Use command - buy to buy DsawCoin!")
      print(Fore.GREEN , "Use command - sell to sell DsawCoin!")
      print(Fore.GREEN , "Use command - about to know more about DsawCoin!")
      print(Fore.GREEN , "Use command - exit to exit the DsawCoin bash!")
      print(Fore.GREEN , "Use command - gen to generate DsawCoin for your account!")
      print(Fore.GREEN , "Use command - bal to get your DsawCoin balance!")
      print(Fore.GREEN , "Use command - balm to get your Money balance!")
    elif i_suck == "about":
      print(Fore.GREEN , "DsawCoin is a fake cryptocurency!")
      print(Fore.GREEN , "This means you can generate it to practice crypto trading with the community!")
      print(Fore.GREEN , "You can generate money using the gen command!")
    elif i_suck == "exit":
      print("")
      print(Fore.BLUE + "Buh,Bye!")
      exit()
    elif i_suck == "gen":
      how_much = input(Fore.GREEN + "How much DsawCoin? [Max 100]:")
      int_token = int(how_much)
      if int_token > 100:
        print(Fore.RED, "Max 100!")
      elif int_token <= 100:
        nah = int(balance[0][0])
        ohno = int_token + nah
        sql = f"UPDATE ID SET balance = {ohno} WHERE balance = {nah}"
        mycursor.execute(sql)
        mydb.commit()
        get_balance = f"SELECT balance FROM ID WHERE name=(%s)" #:(((((
        val = (token_user, )
        balance_getting = mycursor.execute(get_balance, val)
        balance = mycursor.fetchall()
        mydb.commit()
        print(Fore.GREEN, "Transaction complete")

    elif i_suck == "bal":
        get_balance = f"SELECT balance FROM ID WHERE name=(%s)" #:(((((
        val = (token_user, )
        balance_getting = mycursor.execute(get_balance, val)
        balance = mycursor.fetchall()
        mydb.commit()
        print(f"You have {balance[0][0]} DsawCoin")
    elif i_suck == "cp":
      response = requests.get('https://dsaw-coin-price.herokuapp.com/') 
      response_json = response.json()
      ah = response_json["price"]
      print(Fore.GREEN, "The current price of one DsawCoin is" ,ah)
      print(Fore.GREEN, "This changes every 12 hours!")
    elif i_suck == "sell":
      bal_no = int(balance[0][0])
      how = input(f"{Fore.GREEN}How much would you like to sell?:")
      how_int = int(how)
      if how.isdigit:
        if how_int > bal_no:
          print("You don't have that much!")
        elif how_int <= bal_no:
          bal_now = bal_no - how_int
          sql = f"UPDATE ID SET BALANCE ={bal_now} WHERE BALANCE = {bal_no}"
          mycursor.execute(sql)
          mydb.commit()
          response = requests.get('https://dsaw-coin-price.herokuapp.com/') 
          response_json = response.json()
          ah = response_json["price"]
          balm = ah * how_int
          get_balance2 = f"SELECT balance FROM ID WHERE name=(%s)" #:(((((
          val2 = (token_user, )
          balance_getting2 = mycursor.execute(get_balance2, val2)
          balance2 = mycursor.fetchall()
          mydb.commit()
          print(Fore.GREEN , "You currently have" , balance2[0][0] , "DsawCoin")
          print(Fore.GREEN , f"You have {balm} money in your money wallet.")
    elif i_suck == "buy":
      h = input(f"{Fore.GREEN}How much?:")
      hin = int(h)
      response = requests.get('https://dsaw-coin-price.herokuapp.com/') 
      response_json = response.json()
      ah = response_json["price"]
      price_of_buy = hin * ah
      if balm < price_of_buy:
        print(Fore.RED,"You don't have that much in your balm.")
      elif balm > price_of_buy:
        ye_nah_or = input(f"{Fore.GREEN} {price_of_buy} Is the cost, Procced? [Y or N]")
        if ye_nah_or == "Y":
          balm = balm - price_of_buy
          ahh = int(balance[0][0]) + hin
          sql = f"UPDATE ID SET balance = {ahh} WHERE balance = {balance[0][0]}"
          mycursor.execute(sql)
          mydb.commit()
          #print(ahh)
        elif ye_nah_or == "N":
          pass
        else:
          print(Fore.RED, "Err")
    elif i_suck == "balm":
      print(Fore.GREEN, "Your money is store in sessions!")
      print(Fore.GREEN, "Current balance is" , balm)
    else:
      print(Fore.GREEN)
      print(Fore.RED,"Err!")
      print(Fore.GREEN)
      pass




except Exception as e:
  print(e)
  print("")
  #print(Fore.BLUE + "Buh,Bye!")

#a61787d100bdf6b8767f7073de657ffc