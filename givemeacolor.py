import converter as c
import twitter_streaming as s
import tweepy
import time

while 0 < 1:
	random_tweet = ''
	hex_value = []
	x = ''
	auth = tweepy.OAuthHandler('d3BJes2gtaL8MGvzyVEfoJC5T', 'xxiDIGsCteWNOFg7hjPMZFKN9Cc1bJx30sLH3PbzzE0Qlu5VFB')
	auth.set_access_token('2984729385-csAE3jYubfiEljuqimVngWZFH8Ri9Jg50r0Mmgu', 'qCAHB0e4Djt9KCztSk3TWNt0TUd8o5YYh0uRc37mYUo60')

	if __name__ == '__main__':
	    l = s.StdOutListener()
	    stream = tweepy.Stream(auth, l)
	    stream.filter(track=['color'])

	digit_list = c.number_to_list(c.string_to_number(s.random_tweet))

	c.translate_to_binary(0,4,digit_list,random_tweet, hex_value)
	c.translate_to_binary(4,8,digit_list,random_tweet, hex_value)
	c.translate_to_binary(8,12,digit_list,random_tweet, hex_value)
	c.translate_to_binary(12,16,digit_list,random_tweet, hex_value)
	c.translate_to_binary(16,20,digit_list,random_tweet, hex_value)
	c.translate_to_binary(20,25,digit_list,random_tweet, hex_value)

	if len(hex_value) == 6:
		hex_value.insert(0, '#')
		twitter_hex_value = ''.join(hex_value)
		print twitter_hex_value
	else:
		print 'Uh oh.'

	api = tweepy.API(auth)
	api.update_status(twitter_hex_value)

	time.sleep(600)






# take string
# turn that string into a 24 digit int
# take 4 digits at a time and turn into binary using even/odd
# from the binary convert back to integer- will be between 0 and 15
# map the number to the dict
# now you have 6 values when put together is a hex code





