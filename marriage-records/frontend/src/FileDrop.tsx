import { useState, useRef, DragEvent, ChangeEvent } from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

export default function FileDrop() {
  const [files, setFiles] = useState<File[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const [uploadSuccess, setUploadSuccess] = useState(false);

  const handleFilesChange = (event: ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      const newFiles: File[] = Array.from(event.target.files);
      setFiles((prevFiles) => [...prevFiles, ...newFiles]);
    }
  };

  const handleDeleteFile = (index: number) => {
    const newFiles = [...files];
    newFiles.splice(index, 1);
    setFiles(newFiles);
  };

  const handleAddMoreFiles = () => {
    inputRef.current?.click();
  };

  const handleResetFiles = () => {
    setFiles([]); // Reset files array to an empty array
    setUploadSuccess(false); // Reset upload success state
  };

  const uploadFiles = async (filesToUpload: File[]) => {
    const formData = new FormData();
    filesToUpload.forEach((file) => {
      formData.append("file", file);
    });

    try {
      const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        // Handle successful upload if needed
        console.log("Files uploaded successfully");
        setUploadSuccess(true);
      } else {
        // Handle error response
        console.error("Error uploading files");
      }
    } catch (error) {
      // Handle fetch error
      console.error("Error uploading files:", error);
    }
  };

  const handleDragOver = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
  };

  const handleDrop = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    if (event.dataTransfer.files) {
      const newFiles: File[] = Array.from(event.dataTransfer.files);
      setFiles((prevFiles) => [...prevFiles, ...newFiles]);
    }
  };

  return (
    <>
      {uploadSuccess ? (
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
                  </li>
                ))}
              </ul>
              <Button onClick={handleResetFiles} variant="secondary">
                Clear
              </Button>
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
      ) : (
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
          {files.length > 0 && (
            <Card style={{ width: "600px", textAlign: "center" }}>
              <Card.Body>
                <Card.Title>Files:</Card.Title>
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
                <Button onClick={handleAddMoreFiles} variant="secondary">
                  Add More Files
                </Button>
                <input
                  type="file"
                  multiple
                  onChange={handleFilesChange}
                  hidden
                  ref={inputRef}
                />
                <Button
                  onClick={() => uploadFiles(files)}
                  size="lg"
                  style={{
                    width: "300px",
                    display: "block",
                    margin: "0 auto",
                    marginTop: "10px",
                  }}
                >
                  Upload Files
                </Button>
              </Card.Body>
            </Card>
          )}

          {files.length === 0 && (
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
                variant="secondary"
                style={{
                  width: "150px",
                  display: "block",
                  margin: "0 auto",
                }}
              >
                Select Files
              </Button>
            </Card>
          )}
        </div>
      )}
    </>
  );
}
