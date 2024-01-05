import NavBar from "./Navbar";
import Checkboxes from "./Checkboxes";
import FileDrop from "./FileDrop";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import "bootstrap/dist/css/bootstrap.css";
import { Button } from "react-bootstrap";

const App = () => {
  const handleExtraction = async () => {
    try {
      const response = await fetch("http://localhost:5000/extract", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // You can pass data to Flask here if needed
        body: JSON.stringify({
          /* Your data */
        }),
      });
      const data = await response.json();
      console.log(data); // Log the response from Flask
    } catch (error) {
      console.error("Error extracting:", error);
    }
  };
  return (
    <div
      style={{
        paddingTop: "10px",
      }}
    >
      <NavBar />
      <hr
        style={{
          background: "black",
          color: "black",
          borderColor: "black",
          height: "3px",
        }}
      />
      <h3
        style={{
          paddingLeft: "100px",
        }}
      >
        Extraction tool{" "}
      </h3>
      <hr
        style={{
          background: "black",
          color: "black",
          borderColor: "black",
          height: "3px",
        }}
      />
      <div
        style={{
          paddingTop: "20px",
          paddingLeft: "200px",
          paddingRight: "200px",
          paddingBottom: "20px",
        }}
      >
        <p>
          Genealogical research is beneficial for many studies relating to
          migration, family health history knowledge discovery, and insight into
          demographics. However, due to the physical degradation of these
          historical documents and the substantial volume, the development of
          transcribing records to online data files/bases is tedious and
          time-consuming. Our group worked to develop a machine learning YOLOv8
          model that creates a virtual spreadsheet to reduce the human load on
          transcribing these documents and increase the availability of the data
          for genealogical research .
        </p>
        <hr
          style={{
            background: "black",
            color: "black",
            borderColor: "black",
            height: "3px",
          }}
        />
      </div>

      <Row className="justify-content-center">
        <Col md={4} className="d-flex justify-content-center">
          <FileDrop />
        </Col>
        <Col
          md={8}
          className="d-flex justify-content-center align-items-center"
        >
          <div>
            <Checkboxes />
          </div>
        </Col>
      </Row>
      <div
        style={{
          paddingTop: "20px",
          paddingLeft: "200px",
          paddingRight: "200px",
        }}
      >
        <hr
          style={{
            background: "black",
            color: "black",
            borderColor: "black",
            height: "3px",
          }}
        />
      </div>

      <div
        className="d-flex justify-content-center"
        style={{ paddingTop: "25px", paddingBottom: "40px" }}
      >
        <Button style={{ width: "200px" }} onClick={handleExtraction}>
          Extract
        </Button>
      </div>
    </div>
  );
};
export default App;
