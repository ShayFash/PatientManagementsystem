import React from 'react';
import {Link, useParams} from 'react-router-dom';
import PatientProfileContainer from './PatientProfileContainer';

function Prescription() {
    let {num} = useParams();
    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
            <form style={{height: "200px"}}>
                <br />
                <input type="text" placeholder="Medication with Dosage"
                style={{width:"70%", fontSize: "16px"}}
                >
                </input>
                <br/>
                <div className="horizontalDivider" style={{width: "50%"}}/>
                <Link to={`/patient/${num}`}>
                    <button className="navBarButton"
                    style={{marginTop: "5%"}} 
                    >Request</button>
                </Link>
            </form>
        </div>
    )
}

export default Prescription;