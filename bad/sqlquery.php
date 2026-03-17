<?php 

use Symfony\Component\HttpFoundation\Request;

class Controller
{
    /**
     * @var \Doctrine\DBAL\Connection
     */
    protected $connection;

    public function sqlQuery1(Request $request)
    {
          $userId = $request->get('id');
        $sql = "SELECT email FROM user WHERE id='$userId'";
        $statement = $this->connection->prepare($sql);
        $statement->execute();
        $username = $statement->fetchColumn();
        return $this->json(['email' => $username]);
    }
    
        public function anotherSqlQuery1(Request $request)
    {
        $userId = $request->get('name');
        #$sql = "SELECT username FROM user WHERE id='$userId'";
        $sql = "SELECT username FROM user";
        $statement = $this->connection->prepare($sql);
        $statement->execute();
        $username = $statement->fetchColumn();
        return $this->json(['email' => $username]);
    }
}
?>
