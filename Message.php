<?php
if(isset($_GET["submit"])){
    $Prenom = $_GET['Prenom'];
    $Nom = $_GET['Nom'];
    $Email = $_GET['Email'];
    $Telephone = $_GET['Telephone'];
    $Message = $_GET['Message'];

    $connection = mysqli_connect("localhost", "root", "", "portfolio");
    $req = "INSERT INTO `message`(`Prenom`, `Nom`, `Email`, `Telephone`, `Message`) VALUES ('$Prenom','$Nom','$Email','$Telephone','$Message')";
    $result = mysqli_query($connection,$req);
    echo "votre message a été envoyé avec succés";
}else{
    echo "erreur de connection";
}

?>