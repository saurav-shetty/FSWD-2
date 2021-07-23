<?php
error_reporting(0);
if(isset($_POST)) {
	$Name = $_POST['Name'];
    $phone = $_POST['phone'];
	$email = $_POST['email'];
	$subject = $_POST['subject'];
	$message = $_POST['message'];
	$conn = new mysqli('localhost','root','','project-2');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("INSERT INTO `contact_us` (`Name`,'Phone', `Email`, `subject`, `message`) VALUES (?, ?, ?, ?, ?)");
		$stmt->bind_param("issss",$Name, $phone, $email, $subject, $message);
		$execval = $stmt->execute();
		echo $execval;
		echo "Your Message was successfully submitted";
		$stmt->close();
		$conn->close();
	}
}
else { echo "No Data";}
?>