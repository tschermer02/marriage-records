import { useState, useRef, DragEvent, ChangeEvent } from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

export default function FileDrop() {
  const [files, setFiles] = useState<File[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleDragOver = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
  };

  const handleDrop = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    const newFiles = event.dataTransfer.files;
    if (newFiles) {
      const updatedFiles = Array.from(newFiles);
      setFiles((prevFiles) => [...prevFiles, ...updatedFiles]);
    }
  };

  const handleAddMoreFiles = () => {
    inputRef.current?.click();
  };

  const handleDeleteFile = (index: number) => {
    setFiles((prevFiles) => {
      const updatedFiles = [...prevFiles];
      updatedFiles.splice(index, 1);
      return updatedFiles;
    });
  };

  const handleFilesChange = async (event: ChangeEvent<HTMLInputElement>) => {
    const newFiles = event.target.files;
    if (newFiles) {
      const formData = new FormData();
      Array.from(newFiles).forEach((file) => {
        formData.append("file", file);
      });

      try {
        const response = await fetch("http://127.0.0.1:5000/upload", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          // Handle successful upload if needed
          console.log("Files uploaded successfully");
        } else {
          // Handle error response
          console.error("Error uploading files");
        }
      } catch (error) {
        // Handle fetch error
        console.error("Error uploading files:", error);
      }

      const updatedFiles = Array.from(newFiles);
      setFiles((prevFiles) => [...prevFiles, ...updatedFiles]);
    }
  };

  const handleUploadButtonClick = async () => {
    const formData = new FormData();
    files.forEach((file) => {
      formData.append("file", file);
    });

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        // Handle successful upload if needed
        console.log("Files uploaded successfully");
      } else {
        // Handle error response
        console.error("Error uploading files");
      }
    } catch (error) {
      // Handle fetch error
      console.error("Error uploading files:", error);
    }
  };

  return (
    <>
      {files.length > 0 && (
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            paddingLeft: "300px",
          }}
        >
          <Card style={{ width: "600px", textAlign: "center" }}>
            <Card.Body>
              <Card.Title>Uploaded Files:</Card.Title>
              <ul style={{ listStyle: "none", padding: 0 }}>
                {files.map((file, idx) => (
                  <li key={idx} style={{ paddingBottom: "5px" }}>
                    {file.name}
                    <Button
                      variant="danger"
                      size="sm"
                      onClick={() => handleDeleteFile(idx)}
                      style={{ marginLeft: "10px" }}
                    >
                      Delete
                    </Button>
                  </li>
                ))}
              </ul>
              <Button onClick={handleAddMoreFiles}>Add More Files</Button>
              <input
                type="file"
                multiple
                onChange={handleFilesChange}
                hidden
                ref={inputRef}
              />
            </Card.Body>
          </Card>
        </div>
      )}

      {files.length === 0 && (
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            paddingLeft: "300px",
          }}
          onDragOver={handleDragOver}
          onDrop={handleDrop}
        >
          <Card style={{ width: "600px", paddingBottom: "20px" }}>
            <h3
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                paddingTop: "20px",
              }}
            >
              Drag and Drop Files to Upload
            </h3>
            <h5
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <img
                src={"cloud_file_upload_server_icon_196427.jpg"}
                style={{ maxWidth: "100%", maxHeight: "200px" }}
                draggable="false"
              />
            </h5>
            <h5
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              Or
            </h5>
            <input
              type="file"
              multiple
              onChange={handleFilesChange}
              hidden
              ref={inputRef}
            />
            <Button
              onClick={() => inputRef.current?.click()}
              style={{
                width: "150px",
                display: "block",
                margin: "0 auto",
              }}
            >
              Select Files
            </Button>
          </Card>
        </div>
      )}
      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <Button onClick={handleUploadButtonClick} disabled={files.length === 0}>
          Upload Files
        </Button>
      </div>
    </>
  );
}
