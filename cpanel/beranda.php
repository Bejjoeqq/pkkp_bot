<?php include 'header.php'; ?>
<div class="container-fluid body">
	<div class="row">
		<div class="col-lg-2 sidebar">
			<?php include 'sidebar.php'; ?>
		</div>
		<div class="col-lg-10 main-content">
			<div class="panel panel-default">
				<div class="panel-body">
					<div class="row">
						<div class="col-md-12">
							<h2 class="page-header">Selamat datang, <strong><?php echo $_SESSION['nm_admin']; ?></strong></h2>
						</div>
					</div>
					<div class="row">
						<div class="col-md-12">
							<div class="col-sm-3 big-icon">
								<a href="admin.php">
									<span class="fa fa-user fa-5x"></span>
									<h4>Admin</h4>
								</a>
							</div>
							<div class="col-sm-3 big-icon">
								<a href="peserta.php">
									<span class="fa fa-book fa-5x"></span>
									<h4>Peserta</h4>
								</a>
							</div>
							<div class="col-sm-3 big-icon">
								<a href="keyword.php">
									<span class="fa fa-envelope fa-5x"></span>
									<h4>Keyword</h4>
								</a>
							</div>
							<div class="col-sm-3 big-icon">
								<a href="history.php">
									<span class="fa fa-folder-o fa-5x"></span>
									<h4>History</h4>
								</a>
							</div>
						</div>
					</div>
					<?php
					$result = $mysqli->query("SELECT count(*) as total FROM pkkp_daftar");
					$result1 = $mysqli->query("SELECT count(*) as total FROM pkkp_daftar where daftar_status='ya'");
					$result2 = $mysqli->query("SELECT key_word FROM pkkp_key ORDER BY key_count DESC");
					$data = $result->fetch_assoc();
					$data1 = $result1->fetch_assoc();
					$data2 = $result2->fetch_assoc();
					?>
					<div class="row">
						<div class="col-md-12">
							<h3>Jumlah Seluruh Peserta : <strong><?php echo $data["total"] ?></strong></h3>
							<h3>Jumlah Peserta Valid : <strong><?php echo $data1["total"] ?></strong></h3>
							<h3 class="page-header">Keyword Paling Banyak Digunakan :  <strong><?php echo $data2["key_word"] ?></strong></h3>
							<h2>Admin Level</h2>
							<h3>1. Owner > 2. Admin > 3. Content</h3>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<?php include 'footer.php'; ?>