import React from 'react';
import {Link} from 'react-router-dom';

function PatientSearch(props) {
    return (
        <div>
            <div className="horizontalDivider" style={{width: "90%"}} />
            <Link to="/login">
                <button className="navBarButton">Logout</button>
            </Link>
            <form className="homeContainer" style={{padding: "100px", marginBottom: "0px"}}>
                <select className="navBarButton" style={{fontSize: "32px"}}>
                    <option>Alberta</option>
                    <option>British Columbia</option>
                    <option>Manitoba</option>
                    <option>New Brunswick</option>
                    <option>Newfoundland</option>
                    <option>Northwest Territories</option>
                    <option>Nova Scotia</option>
                    <option>Nunavut</option>
                    <option>Ontario</option>
                    <option>Prince Edward Island</option>
                    <option>Quebec</option>
                    <option>Saskatchewan</option>
                    <option>Yukon</option>
                </select>
                <br /><br />
                <input type="text" placeholder="Health Card #" style={{fontSize: "32px"}}></input>
                <br /><br />
                <Link to="/">
                    <button className="homeContainer">Search</button>
                </Link>
            </form>
        </div>
    )
}

export default PatientSearch;