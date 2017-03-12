<?php
if (isset($_Post['button'])){
	exec('sudo python3 /home/pi/Jufo_Bikelight/Release/main.py')
}
?>