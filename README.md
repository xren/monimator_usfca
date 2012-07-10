# USF labmonitor signup script #

1. How to run
`python monimator_usfca.py -i fetch_interval -u username -p password -f first_slot [-s second_slot] [-d debug]`

2. Slot match up  

				Up:Harney 530/535		Down: Harney 235
		Monday:			umon				NA
		TuesDay:		utue				dtue
		Wednesday:		used				NA
		Thursday:		uthu				dthu
		Friday:			ufri				dfri
		Sat_morning:	usat1				dsat1
		Sat_afternoon:	usat2				dsat2
		Sun_morning:	usun1				dsun1
		Sun_afternoon:	usun2				dsun2

3. Example
Here I am going to sign up by sending requests every one second with username *john* and password *yoface*. And I'm interested in working downstairs every Friday night.

`python monimator_usfca.py -i 1 -u john -p yoface -f dfri`

Let's roll!
