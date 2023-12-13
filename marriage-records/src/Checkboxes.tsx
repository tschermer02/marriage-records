import Form from "react-bootstrap/Form";

export default function Checkboxes() {
  return (
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
  );
}
