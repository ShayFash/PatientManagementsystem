import React, {useState} from 'react';
import {Link} from 'react-router-dom';

function PatientSearch(props) {
    const [healthNumber, setHealthNumber] = useState("");
    const [location, setLocation] = useState("");

    function changeNumber(event) {
        const {value} = event.target;
        setHealthNumber(value);
    }
    
    function changeLocation(event) {
        const {value} = event.target;
        setLocation(value);
    }

    console.log(location); // placeholder so that the location variable doesnt throw a "not being used" message at me

    return (
        <div>
            <div className="horizontalDivider" style={{width: "90%"}} />
            <Link to="/login">
                <button className="navBarButton">Logout</button>
            </Link>
            <form className="homeContainer" style={{padding: "100px", marginBottom: "0px"}}>
                <select className="navBarButton" style={{fontSize: "32px"}} onChange={changeLocation}>
                    <option selected disabled>Province</option>
                    <option value="Alberta">Alberta</option>
                    <option value="British Columbia">British Columbia</option>
                    <option value="Manitoba">Manitoba</option>
                    <option value="New Brunswick">New Brunswick</option>
                    <option value="Newfoundland">Newfoundland</option>
                    <option value="Northwest Territories">Northwest Territories</option>
                    <option value="Nova Scotia">Nova Scotia</option>
                    <option value="Nunavut">Nunavut</option>
                    <option value="Ontario">Ontario</option>
                    <option value="Prince Edward Island">Prince Edward Island</option>
                    <option value="Quebec">Quebec</option>
                    <option value="Saskatchewan">Saskatchewan</option>
                    <option value="Yukon">Yukon</option>
                </select>
                <br /><br />
                <input type="text" 
                placeholder="Health Card #" 
                style={{fontSize: "32px"}} 
                value={healthNumber}
                onChange={changeNumber}></input>
                <br /><br />
                <Link to="/">
                    <button className="navBarButton">Search</button>
                </Link>
            </form>
        </div>
    )
}

export default PatientSearch;