<?php
include '../config/koneksi.php';

$data_qry = $mysqli->query("SELECT daftar_status FROM pkkp_daftar WHERE daftar_idtele = '$_GET[id]'") or die ($mysqli->error);
$data = $data_qry->fetch_assoc();

if ($data['daftar_status']=='tidak') {
	$update_qry = $mysqli->query("UPDATE pkkp_daftar SET daftar_status = 'ya' WHERE daftar_idtele = '$_GET[id]'");
} else {
	$update_qry = $mysqli->query("UPDATE pkkp_daftar SET daftar_status = 'tidak' WHERE daftar_idtele = '$_GET[id]'");
}

if (!$update_qry) {
	die("Error updating 'buku_tamu': ".$mysqli->error);
} else {
	header("location:peserta.php");
}