import Form from "react-bootstrap/Form";
import { Card } from "react-bootstrap";

export default function Checkboxes() {
  return (
    <div>
      <Card
        style={{
          width: "500px",
          paddingLeft: "20px",
          paddingTop: "60px",
          paddingBottom: "60px",
        }}
      >
        <h5>Select which words you would like to extract: </h5>
        <Form>
          <div>
            <Form.Check // prettier-ignore
              id={"milleottocentosettanta"}
              label={"milleottocentosettanta"}
            />
            <Form.Check // prettier-ignore
              id={"1"}
              label={"1"}
            />
            <Form.Check // prettier-ignore
              id={"1"}
              label={"2"}
            />
            <Form.Check // prettier-ignore
              id={"residente"}
              label={"residente"}
            />
            <Form.Check // prettier-ignore
              id={"residente2"}
              label={"residente"}
            />
            <Form.Check // prettier-ignore
              id={"addi"}
              label={"addi"}
            />
            <Form.Check // prettier-ignore
              id={"anni"}
              label={"anni"}
            />
            <Form.Check // prettier-ignore
              id={"di"}
              label={"di"}
            />
          </div>
        </Form>
      </Card>
    </div>
  );
}
