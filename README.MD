# Get count mention about something in VK.COM 
The project get mentions for previous days and make plot with it. 


## Description
The code: 
The project get mentions for previous days and make plot with it. 

* The project uses:   
  * [VK API](https://vk.com/dev).
  

## Requirements
Python >=3.7  
Register application on [VK API](https://vk.com/dev) ang get API access token.  
 
Create file '.env' and add the code:
```
VK_ACCESS_TOKEN = your_vk_app_token
```

Install requirements modules:
```
pip install -r requirements.txt	
```


### How to use

Install requirements.  
Open and run 'main.py'.
```
python main.py	
```


## Additional information
You have to enter your search request. For it change variable 'search_request' in **main()** function:
```
search_request = your_search_request
```
Also you can change for how many days you want to get statistic. For it change variable 'previous_days' in **main()** function:
```
day_range = 30
```

* How to create [vk.com](https://vk.com/apps?act=manage) app and vk access token:
  * Go to page [vk.com/apps](https://vk.com/apps?act=manage)
  * Click on 'Creat App' button
  * Fill fields
  * Change platform 'Standalone'
  * Copy your key from 'Service token' field


## Project goal

The code was written for educational purpose on online course for Api developers [Devman](http://dvmn.org). 
