class Login:


    def __init__(self,Rrow,URL):

     
     self.Rrow = Rrow
     self.URL= URL


    def loginToApp(self):

        rrow = self.Rrow
        URL = self.URL

        print (rrow)
       #for index, row in df1.iterrows():
        if rrow.loc["TestCase"] == 'Login to Site':
            print ("kitmoduleFound")
            TestCase = rrow.loc["TestCase"]
            Username = rrow.loc["Parameter1"]
            Password = rrow.loc["Parameter2"]
            print(TestCase,Username,Password,URL)
            #kititem = kt(df1,df2)
            #continue;
