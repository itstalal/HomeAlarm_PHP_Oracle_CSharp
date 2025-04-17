<?php
header('Content-Type: application/json');

// Connexion Oracle avec PDO
$dsn = "oci:dbname=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=ORCL)));charset=AL32UTF8";
$user = "system";
$pass = "system";

try {
    $db = new PDO($dsn, $user, $pass);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(["error" => "Connexion échouée : " . $e->getMessage()]);
    exit;
}

$scriptName = $_SERVER['SCRIPT_NAME'];
$requestUri = $_SERVER['REQUEST_URI'];
$path = str_replace($scriptName, '', parse_url($requestUri, PHP_URL_PATH));
$method = $_SERVER['REQUEST_METHOD'];

// API
function getAlarmStatus($db) {
    $stmt = $db->prepare("SELECT zone1, zone2, zone3, zone4 FROM Alarmsyst WHERE id = 1");
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getEtatAlarm($db) {
    $stmt = $db->prepare("SELECT etat FROM Alarmsyst WHERE id = 1");
    $stmt->execute();
    $res = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($res && isset($res['ETAT'])) {
        return ['etat' => (int)$res['ETAT']];
    } else {
        return ['etat' => null, 'error' => 'État non trouvé ou colonne manquante'];
    }
}

function updateEtatAlarm($db) {
    // Récupérer l'état actuel de l'alarme
    $stmt = $db->prepare("SELECT etat FROM Alarmsyst WHERE id = 1");
    $stmt->execute();
    $etat = intval($stmt->fetchColumn());

    // Inverser l'état : 1 => 0, 0 => 1
    $newEtat = $etat === 1 ? 0 : 1;

    // Mettre à jour l'état de l'alarme
    $update = $db->prepare("UPDATE Alarmsyst SET etat = :etat, timestamp = CURRENT_TIMESTAMP WHERE id = 1");
    $update->execute([':etat' => $newEtat]);

    // Si l'alarme est désactivée (0), mettre toutes les zones à 0 aussi
    if ($newEtat === 0) {
        $updateZones = $db->prepare("UPDATE Alarmsyst SET zone1 = 0, zone2 = 0, zone3 = 0, zone4 = 0 WHERE id = 1");
        $updateZones->execute();
    }

    return ['updated' => true, 'etat' => $newEtat];
}


function updateZone($db, $zoneNumber) {
    $zone = 'zone' . intval($zoneNumber);
    $stmt = $db->prepare("SELECT $zone FROM Alarmsyst WHERE id = 1");
    $stmt->execute();
    $current = intval($stmt->fetchColumn());
    $new = $current === 1 ? 0 : 1;

    $update = $db->prepare("UPDATE Alarmsyst SET $zone = :val, timestamp = CURRENT_TIMESTAMP WHERE id = 1");
    $update->execute([':val' => $new]);

    return ['updated' => true, 'zone' => $zone, 'newValue' => $new];
}

// Routes
if ($method === 'GET' && $path === '/zones') {
    echo json_encode(getAlarmStatus($db));

} elseif ($method === 'GET' && $path === '/etat') {
    echo json_encode(getEtatAlarm($db));

} elseif ($method === 'PUT' && preg_match('#^/zones/(\d+)$#', $path, $matches)) {
    $zone = intval($matches[1]);
    echo json_encode(updateZone($db, $zone));

} elseif ($method === 'PUT' && $path === '/etat/update') {
    echo json_encode(updateEtatAlarm($db));

} elseif ($method === 'PUT' && $path === '/reset') {
    $update = $db->prepare("UPDATE Alarmsyst SET zone1 = 0, zone2 = 0, zone3 = 0, zone4 = 0, timestamp = CURRENT_TIMESTAMP WHERE id = 1");
    $update->execute();
    echo json_encode(['reset' => true]);
}else {
    http_response_code(404);
    echo json_encode(['error' => 'Route non trouvée', 'path' => $path]);
}
