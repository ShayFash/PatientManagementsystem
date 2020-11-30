import React, {useState} from 'react';
import PatientProfileContainer from './PatientProfileContainer';

function BloodWorkForm() {
    const [requested, setRequested] = useState(false);

    function changeRequested(event) {
        setRequested(true);
    }

    const bloodWorkTypes = ["FSH/LH", "STI", "H1AC", "etc"];
    const bloodWorkElements = []
    for (var i = 0; i < bloodWorkTypes.length; i++) {
        bloodWorkElements.push(
            <div>
                <input type="checkbox"></input>
                <span style={{fontSize: "24px"}}>{bloodWorkTypes[i]}</span>
                <br /><br />
            </div>
        )
    }
    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <div style={{textAlign: "left", marginLeft: "5%"}}>
                <h1>Blood Work{requested && " -- request submitted"}</h1>
                {bloodWorkElements}
                <button className="navBarButton" onClick={changeRequested} >Request</button>
            </div>
        </div>
    )
}

function ImagingForm() {
    const [requested, setRequested] = useState(false);

    function changeRequested(event) {
        setRequested(true);
    }

    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <div style={{textAlign: "left", marginLeft: "5%"}}>
                <h1>Imaging{requested && " -- request submitted"}</h1>
                <button className="navBarButton" onClick={changeRequested} >Request</button>
            </div>
        </div>
    )
}

function ECGForm() {
    const [requested, setRequested] = useState(false);

    function changeRequested(event) {
        setRequested(true);
    }

    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <div style={{textAlign: "left", marginLeft: "5%"}}>
                <h1>ECG{requested && " -- request submitted"}</h1>
                <button className="navBarButton" onClick={changeRequested} >Request</button>
            </div>
        </div>
    )
}

export {BloodWorkForm, ImagingForm, ECGForm};