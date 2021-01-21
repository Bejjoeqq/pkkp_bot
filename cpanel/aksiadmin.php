<?php
include '../config/koneksi.php';

session_start();

$act = $_GET['act'];

switch ($act) {
	case 'tambah':

		if (trim($_POST['kategori'])=="" || trim($_POST['kategori2'])=="") {
			$message = 'Tidak ada data yang ditambahkan';
		}

		$kategori = $_POST['kategori'];
		$kategori2 = $_POST['kategori2'];

		if (!isset($message)) {
			$insert_sql = "INSERT INTO pkkp_admin(admin_username, admin_password, admin_level) VALUES('$kategori','".md5($kategori2)."',3);";

			$insert_qry = $mysqli->query($insert_sql);

			if ($insert_qry) {
				echo "<script>alert('Data Berhasil Ditambah'); window.location = 'admin.php'</script>";
			} else {
				echo $mysqli->error;
			}
		} else {

			echo "<script>alert('Data Gagal Ditambah'); window.location = 'admin.php'</script>";

		}

		break;

	case 'hapus':
			$del_kat_qry = "DELETE FROM pkkp_admin WHERE admin_id = '".$_GET['id']."'";

			$del_kat = $mysqli->query($del_kat_qry);

			if ($del_kat) {
				echo "<script>alert('Data Berhasil Dihapus'); window.location = 'admin.php'</script>";
			} else {
				echo $mysqli->error;
			}

		break;

	default:

		header('location: admin.php');

		break;
}