<! Version 1.8>
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Sensorproject</title>
    <link href="dashboard.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }
  
      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
  
      .b-example-divider {
        height: 3rem;
        background-color: rgba(0, 0, 0, .1);
        border: solid rgba(0, 0, 0, .15);
        border-width: 1px 0;
        box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
      }
  
      .b-example-vr {
        flex-shrink: 0;
        width: 1.5rem;
        height: 100vh;
      }
  
      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }
  
      .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
      }
  
      .nav-scroller .nav {
        display: flex;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }
    </style>

  </head>

  <body>
    <! Header>
    <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
      <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6">Sensorproject Dashboard</a>
    </header>


    <! Body>
    <div class="container-fluid">
      <div class="row">
        <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
          <div class="position-sticky pt-3 sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">
                  <span data-feather="home" class="align-text-bottom"></span>
                  Dashboard
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="https://github.com/SensorProjectSW" target="_blank">
                  <span data-feather="file" class="align-text-bottom"></span>
                  Github
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="bar-chart-2" class="align-text-bottom"></span>
                  Reports
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="layers" class="align-text-bottom"></span>
                  Other Databases
                </a>
              </li>
            </ul>
          </div>
        </nav>
    
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
            <h1 class="h2">CO2-Anteil der Luft - Verlauf</h1>
          </div>
    
          <?php
            // Connect to the sqlite database
            $db = new SQLite3("sensors.db");

            // Query the sensors table
            $result = $db->query("SELECT * FROM Sensors");

            // Print table headers
            echo "<table>
              <tr>
                <th>ID</th>
                <th>Sensor Name</th>
                <th>Sensor Type</th>
                <th>Value</th>
                <th>Timestamp</th>
                <th>Location</th>
              </tr>";

            // Print each row of the table
            while ($row = $result->fetchArray()) {
              echo "<tr>
                <td>{$row['Datum']}</td>
                <td>{$row['Zeit']}</td>
                <td>{$row['eco2']}</td>
                <td>{$row['tvoc']}</td>
                <td>{$row['humidity']}</td>
                <td>{$row['temperature']}</td>
              </tr>";
            }

            echo "</table>";

            // Close the database connection
            $db->close();
          ?>

          <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas>
    
          <h2>Section title</h2>
          <div class="table-responsive">
            <table class="table table-striped table-sm">
              <thead>
                <tr>
                  <th scope="col">Datum</th>
                  <th scope="col">Uhrzeit</th>
                  <th scope="col">eCO2</th>
                  <th scope="col">TVOC</th>
                  <th scope="col">Temperature</th>
                  <th scope="col">Humidity</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1,001</td>
                  <td>random</td>
                  <td>data</td>
                  <td>placeholder</td>
                  <td>text</td>
                  <td>layout</td>
                </tr>
                <tr>
                  <td>1,002</td>
                  <td>placeholder</td>
                  <td>irrelevant</td>
                  <td>visual</td>
                  <td>layout</td>
                  <td>layout</td>
                </tr>
              </tbody>
            </table>
          </div>
        </main>
      </div>
    </div>
    
  <script src="../assets/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js" integrity="sha384-uO3SXW5IuS1ZpFPKugNNWqTZRRglnUJK6UAZ/gxOX80nxEkN9NcGZTftn6RzhGWE" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.4/dist/Chart.min.js" integrity="sha384-zNy6FEbO50N+Cg5wap8IKA4M/ZnLJgzc6w2NqACZaK0u0FXfOWRRJOnQtpZun8ha" crossorigin="anonymous"></script><script src="dashboard.js"></script>
  </body>
</html>
