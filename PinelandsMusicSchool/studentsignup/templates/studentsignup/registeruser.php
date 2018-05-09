<?php
#$pdo = new PDO('mysql:host=localhost;dbname=puppies', 'min', 'Secret!');
#$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

#try {
#	$db = $pdo->query('SELECT ID, PuppyName, BreedName, Description, Price, Picture, Sold '.
#	'FROM animals, breeds '.
#	'WHERE animals.BreedID = breeds.Breed AND Sold = 0');
#} catch (PDOException $e) {
#	echo $e->getMessage();
#}

#try {
#	$allBreeds = $pdo->query('SELECT *'.
#	'FROM breeds ');
#} catch (PDOException $e) {
#	echo $e->getMessage();
#}

$stmt = $pdo->prepare('INSERT INTO animals (PuppyName, BreedID, Description, Price, Picture, Sold)
						VALUES (:PuppyName, :BreedID, :Description, :Price, :Picture, :Sold)');
$stmt->bindValue(':PuppyName', $_POST["PuppyName"]);
$stmt->bindValue(':BreedID', $_POST["BreedID"]);
$stmt->bindValue(':Description', $_POST["Description"]);
$stmt->bindValue(':Price', $_POST["Price"]);
$stmt->bindValue(':Picture', $_POST["Picture"]);
$stmt->bindValue(':Sold', 0);
$stmt->execute();
?>