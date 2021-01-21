<?php
include '../config/koneksi.php';

$username=$mysqli->real_escape_string(stripslashes(strip_tags(htmlspecialchars($_POST['username'],ENT_QUOTES))));
$password=$mysqli->real_escape_string(stripslashes(strip_tags(htmlspecialchars($_POST['password'],ENT_QUOTES))));

$result = $mysqli->query("SELECT * FROM pkkp_admin WHERE admin_username='".$username."' AND admin_password='".md5($password)."'");
$data = $result->fetch_assoc();

if($result->num_rows) {
	session_start();
	$_SESSION['admin'] = 1;
	$_SESSION['id_admin'] = $data['admin_id'];
	$_SESSION['nm_admin'] = $data['admin_username'];
	$_SESSION['level'] = $data['admin_level'];
	header('location:beranda.php');
}
else {
	header('location:index.php?failed=1');
}