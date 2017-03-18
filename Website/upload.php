<?php

$upload_folder = '/home/pi/Bilder/'; //Das Upload-Verzeichnis
$filename = pathinfo($_FILES['datei']['name'], PATHINFO_FILENAME);
$extension = strtolower(pathinfo($_FILES['datei']['name'], PATHINFO_EXTENSION));

//Überprüfung der Dateiendung
$allowed_extensions = array('png', 'jpg', 'jpeg');
if(!in_array($extension, $allowed_extensions)) {
 die("Ungültige Dateiendung. Nur png, jpg und jpeg-Dateien sind erlaubt");
}
exec('rm /home/pi/Bilder/Bild.*');
exec('rm /home/pi/Bilder/Temp.*');
//Pfad zum Upload
$temp_path = $upload_folder.'Temp'.'.'.$extension;
$new_path = $upload_folder.'Bild'.'.';

move_uploaded_file($_FILES['datei']['tmp_name'], $temp_path);


function resize_imagejpg($file, $w, $h) {
   list($width, $height) = getimagesize($file);
   $src = imagecreatefromjpeg($file);
   $dst = imagecreatetruecolor($w, $h);
   imagecopyresampled($dst, $src, 0, 0, 0, 0, $w, $h, $width, $height);
   return $dst;
}

 // for png
function resize_imagepng($file, $w, $h) {
   list($width, $height) = getimagesize($file);
   $src = imagecreatefrompng($file);
   $dst = imagecreatetruecolor($w, $h);
   imagecopyresampled($dst, $src, 0, 0, 0, 0, $w, $h, $width, $height);
   return $dst;
}
function resizeImage($file, $w, $h, $extension, $new_path){

	switch ($extension) {
		case 'jpeg':
			$pic = resize_imagejpg($file, $w, $h);
			break;
		case 'jpg':
			$pic = resize_imagejpg($file, $w, $h);
		case 'png':
			$pic = resize_imagepng($file, $w, $h);
			
			break;
		default:
			die('Der gegebene Dateityp(' . $extension . ') wird nicht unterstützt!!');
			break;
	}

	imagepng($pic, $new_path.'png', 9);
	imagedestroy($pic);
}

resizeImage($temp_path, 90, 90, $extension, $new_path);
echo 'Bild erfolgreich hochgeladen: </a href="'.$new_path.'">'.$new_path.'</a>';
echo '<img src="/home/pi/Bilder/Bild.png">'
#exec('rm /home/pi/Bilder/Temp.*');
?>