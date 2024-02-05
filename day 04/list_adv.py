#[].

menu = ["커피", "빵", "주스"]
menu.append("샌드위치")
menu.remove("주스")
menu.sort() # sort는 정렬
print(menu)

numList = [1,2,3,4,5]
numList.reverse() #뒤집기
print(numList)


# 영어로 된 뉴스기사를 가져오고, 단어별로 정렬해!

# news = """Lee Jung-hoo, 26, new San Francisco Giants outfielder, has taken the first step toward conquering Major League Baseball (MLB). Lee left for the U.S. through Incheon International Airport on February 1.
#
# Lee, who signed a six-year, US$113 million contract with the San Francisco Giants in December last year, will begin preparations for the new season in earnest in the U.S. The Giant's players will gear up for the new season at its spring training camp site in Scottsdale, Arizona.
#
#
# The airport was packed with dozens of reporters and fans. "I've always left the country with my teammates, but now that I'm flying out alone and being interviewed by myself, I feel like it's real," Lee said.
#
# Lee, who has been training indoors in Korea to raise his condition, will challenge the U.S. baseball league with a healthy body. He said, "I'm in good shape and my injured ankle where I had surgery last year is also great. Now that I have to go straight into the real game, I think I just need to learn my sense of the real game," expressing his confidence.
#
# close
# Lee was looking forward to facing his best friend Kim Ha-seong of the San Diego Padres in the MLB. The Padres and the Giants will meet in San Diego's home opener at Petco Park on March 29 for the first time in the upcoming regular season. "There's nothing personal about it, and it's just player versus player, so I'll definitely catch Kim’s ball even with my teeth," said Lee, evoking a laugh.
#
# He said he is very excited to face major league pitchers. “Kim told me to come and feel their balls because I’m going to see the balls I have never seen before," Lee said, adding, "As long as they don't hit me, here's nothing to be afraid of. When I go to the batter's box, I will think that there is a ball like this, and I will try harder to hit the ball.”
#
# He was also looking forward to meeting Japanese pitcher Yoshinobu Yamamoto, who moved to the Los Angeles Dodgers this winter. "I've come to belong to the same National League as Yamamoto. I'm curious about how it would feel when I meet him in the national team and the league, and I want to hit his ball," Lee said.
#
# Lee said that he recently had an online meeting with the coaching staff, including manager Bob Melvin. "I felt grateful that he told me that he would help me with everything in adjusting to the new team. I have to prepare well and repay their expectations.”
#
# Lee told his fans, "I will continue to work hard until I retire so that I can repay your love and expectations and I will do my best to perform as I did in Korea."""
#
# news.sort()
# str(print(news))

article """Lee Jung-hoo, 26, new San Francisco Giants outfielder, has taken the first step toward conquering Major League Baseball (MLB). Lee left for the U.S. through Incheon International Airport on February 1.

Lee, who signed a six-year, US$113 million contract with the San Francisco Giants in December last year, will begin preparations for the new season in earnest in the U.S. The Giant's players will gear up for the new season at its spring training camp site in Scottsdale, Arizona.

 
The airport was packed with dozens of reporters and fans. "I've always left the country with my teammates, but now that I'm flying out alone and being interviewed by myself, I feel like it's real," Lee said.

Lee, who has been training indoors in Korea to raise his condition, will challenge the U.S. baseball league with a healthy body. He said, "I'm in good shape and my injured ankle where I had surgery last year is also great. Now that I have to go straight into the real game, I think I just need to learn my sense of the real game," expressing his confidence.

close
Lee was looking forward to facing his best friend Kim Ha-seong of the San Diego Padres in the MLB. The Padres and the Giants will meet in San Diego's home opener at Petco Park on March 29 for the first time in the upcoming regular season. "There's nothing personal about it, and it's just player versus player, so I'll definitely catch Kim’s ball even with my teeth," said Lee, evoking a laugh.

He said he is very excited to face major league pitchers. “Kim told me to come and feel their balls because I’m going to see the balls I have never seen before," Lee said, adding, "As long as they don't hit me, here's nothing to be afraid of. When I go to the batter's box, I will think that there is a ball like this, and I will try harder to hit the ball.”

He was also looking forward to meeting Japanese pitcher Yoshinobu Yamamoto, who moved to the Los Angeles Dodgers this winter. "I've come to belong to the same National League as Yamamoto. I'm curious about how it would feel when I meet him in the national team and the league, and I want to hit his ball," Lee said.

Lee said that he recently had an online meeting with the coaching staff, including manager Bob Melvin. "I felt grateful that he told me that he would help me with everything in adjusting to the new team. I have to prepare well and repay their expectations.”

Lee told his fans, "I will continue to work hard until I retire so that I can repay your love and expectations and I will do my best to perform as I did in Korea.""""

wordList = article.split(" ")
wordList.sort()
print(wordList)