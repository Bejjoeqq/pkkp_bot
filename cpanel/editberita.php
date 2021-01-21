<?php include 'header.php';
$sql_berita = "SELECT berita_id,berita_judul,berita_text FROM pkkp_berita WHERE berita_id='$_GET[id]'";

$qry_berita = $mysqli->query($sql_berita) or die ($mysqli->error);

$data = $qry_berita->fetch_assoc();
?>

<div class="container-fluid body">
	<div class="row">
		<div class="col-lg-2 sidebar">
			<?php include 'sidebar.php'; ?>
		</div>
		<div class="col-lg-10 main-content">
			<div class="panel panel-default">
				<div class="panel-body">
<?php
$var_judul = isset($_POST['berita_judul']) ? $_POST['berita_judul']:$data['berita_judul'];
$var_teksberita = isset($_POST['berita_text']) ? $_POST['berita_text']:$data['berita_text'];
if (isset($_POST['btn_edit'])) {
	$message=array();


    $judul = $mysqli->real_escape_string($_POST['judul']);
    $teks_berita = $_POST['teks_berita'];
    if (count($message)==0) {
    	$insert_sql = "UPDATE pkkp_berita SET berita_judul = '$judul', berita_text = '$teks_berita' WHERE berita_id = '$_GET[id]'";
    	$insert_qry = $mysqli->query($insert_sql) or die ($mysqli->error);

    	echo "<script>alert('Data Berhasil Diperbarui'); window.location = 'berita.php'</script>";
    }

    if (!count($message)==0) {
    	$num=0;
    	foreach ($message as $index => $show_message) {
    		$num++;
?>
		<div class="alert alert-danger alert-dismissable fade in">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            <?php
                echo $show_message;
            ?>
        </div>
<?php
    	}
    }
}
?>
					<div class="row">
						<div class="col-md-12">
							<h2 class="page-header"><i class="fa fa-newspaper-o"></i> Edit Berita</h2>
						</div>
					</div>
					<div class="row">
						<div class="col-md-12">
							<form action="" method="post" enctype="multipart/form-data">
								<div class="col-sm-8">
									<div class="form-group">
										<input type="text" class="form-control" name="judul" placeholder="Judul Berita" value="<?php echo $var_judul; ?>">
									</div>
									<div class="form-group">
										<textarea class="form-control input-sm" name="teks_berita" rows="15" placeholder="Isi Text"><?php echo $var_teksberita; ?></textarea>
									</div>
								</div>
								<div class="col-sm-12">
									<a href="berita.php" class="btn btn-danger btn-sm">
										<i class="fa fa-arrow-left"></i> Kembali
									</a>
									<button class="btn btn-sm btn-primary" type="submit" name="btn_edit">
										<i class="fa fa-check"></i> Edit
									</button>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<script>
    CKEDITOR.replace( 'editor' );
</script>
<?php include 'footer.php'; ?>