import React from 'react';
import Demographics from './Demographics';
import NavBar from './NavBar';
import PatientProfileContainer from './PatientProfileContainer';

function BloodWorkForm() {
    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <div style={{textAlign: "left", marginLeft: "5%"}}>
                <h1>BloodWork</h1>
            </div>
        </div>
    )
}

function ImagingForm() {
    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <form style={{textAlign: "left", marginLeft: "5%"}}>
                <h1>Imaging</h1>
            </form>
        </div>
    )
}

function ECGForm() {
    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <div style={{textAlign: "left", marginLeft: "5%"}}>
                <h1>ECG</h1>
            </div>
        </div>
    )
}

export {BloodWorkForm, ImagingForm, ECGForm};