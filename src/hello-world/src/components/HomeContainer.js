import React from 'react';
import NavBar from './NavBar';
import Demographics from './Demographics';
import PatientProfileContainer from './PatientProfileContainer';

function HomeContainer() {
    return (
        <div className="homeContainer">
            <PatientProfileContainer/>
        </div>
    );
}

export default HomeContainer;