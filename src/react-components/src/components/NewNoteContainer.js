import React, { useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import PatientProfileContainer from './PatientProfileContainer';

function NewNote(props) {
    const [noteText, setNoteText] = useState("");
    const [diagnosisText, setDiagnosisText] = useState("");
    let {num} = useParams();

    function changeNote(event) {
        const {value} = event.target;
        setNoteText(value)
    }

    function changeDiagnosis(event) {
        const {value} = event.target;
        setDiagnosisText(value);
    }

    return (
        <div  className="homeContainer">
            <PatientProfileContainer/>
            <form style={{height: "600px"}}>
                <br />
                <textarea
                placeholder="Insert Text" value={noteText} onChange={changeNote}
                style={{width:"900px", height: "450px", fontSize: "24px"}}
                >
                </textarea>
                <br />
                <input type="text" placeholder="Diagnosis" value={diagnosisText} onChange={changeDiagnosis}
                style={{width:"450px", fontSize: "16px"}}
                >
                </input>
                <div className="horizontalDivider" style={{width: "450px"}}/>
                <br/>
                <Link to={`/patient/${num}`}>
                    <button className="navBarButton"
                    style={{marginTop: "5px"}} 
                    >Post</button>
                </Link>
                <div className="horizontalDivider" style={{width: "830px"}}/>
            </form>
        </div>
    )
}

export default NewNote;