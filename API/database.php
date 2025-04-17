<?php
$dsn = "oci:dbname=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=ORCL)));charset=AL32UTF8";
$user = "system";
$pass = "system";

try {
    $db = new PDO($dsn, $user, $pass);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Fonction pour obtenir l'état complet du système d'alarme
function getAlarmStatus($db) {
    $sql = "SELECT * FROM Alarmsyst";
    $stmt = $db->prepare($sql);
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Fonction pour basculer une zone donnée
function updateAlarmzones($db, $zoneNumber) {
    $columnName = "zone" . intval($zoneNumber);
    
    // Lire la valeur actuelle
    $sql = "SELECT $columnName FROM Alarmsyst WHERE id = :id";
    $stmt = $db->prepare($sql);
    $stmt->execute([':id' => 1]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$row) return ['error' => 'Zone not found'];

    // Oracle retourne directement des entiers, pas besoin de readUInt8
    $currentValue = intval($row[$columnName]);
    $newValue = $currentValue === 1 ? 0 : 1;

    // Mise à jour
    $updateSql = "UPDATE Alarmsyst SET $columnName = :newValue, timestamp = CURRENT_TIMESTAMP WHERE id = :id";
    $updateStmt = $db->prepare($updateSql);
    $updateStmt->execute([
        ':newValue' => $newValue,
        ':id' => 1
    ]);

    return ['updated' => true, 'newValue' => $newValue];
}

// Fonction pour basculer l'état de l'alarme
function updateEtatAlarm($db) {
    $sql = "SELECT etat FROM Alarmsyst WHERE id = :id";
    $stmt = $db->prepare($sql);
    $stmt->execute([':id' => 1]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$row) return ['error' => 'Etat not found'];

    $currentValue = intval($row['etat']);
    $newValue = $currentValue === 1 ? 0 : 1;

    $updateSql = "UPDATE Alarmsyst SET etat = :newValue, timestamp = CURRENT_TIMESTAMP WHERE id = :id";
    $updateStmt = $db->prepare($updateSql);
    $updateStmt->execute([
        ':newValue' => $newValue,
        ':id' => 1
    ]);

    $etat = $newValue === 1 ? 'on' : 'off';
    return ['updated' => true, 'etat' => $etat];
}

function getEtatAlarm($db) {
    $sql = "SELECT etat FROM Alarmsyst WHERE id = :id";
    $stmt = $db->prepare($sql);
    $stmt->execute([':id' => 1]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

?>
