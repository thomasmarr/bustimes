import React, { useState, useEffect } from 'react'
import Arrivals from './Arrivals'
import LoadingWheel from './LoadingWheel'
import ErrorBox from './ErrorBox'

const LiveArrivals = ({ match }) => {
    const [arrivalsArray, setArrivalsArray] = useState()
    const [arrivalsLoading, setArrivalsLoading] = useState(false)
    const [arrivalsError, setArrivalsError] = useState(false)
    const [errorMessage, setErrorMessage] = useState('')

    const fetchArrivals = () => {
        setArrivalsLoading(true)
        setArrivalsError(false)
        const url = match.params.smscode ? `http://localhost:8080/api/live-arrivals/${match.params.smscode}` : match.params.naptanid ? `http://localhost:8080/api/live-arrivals/naptan/${match.params.naptanid}` : null
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    response.json().then(json=>setErrorMessage(json.error))
                    throw Error(response.statusText)
                }
                return response
            })
            .then(response => response.json())
            .then(json => {
                setArrivalsArray(json)
                setArrivalsLoading(false)
                setArrivalsError(false)
                setErrorMessage('')
            })
            .catch(error => {
                setArrivalsArray([])
                console.log(error)
                setArrivalsLoading(false)
                setArrivalsError(true)
            })
    }

    useEffect(fetchArrivals, [match.params.smscode, match.params.naptanid])

    return (
        <div>
            {arrivalsLoading ? <LoadingWheel/> : null}
            {arrivalsError ? <ErrorBox message={errorMessage} refresh={fetchArrivals} /> : null}
            {arrivalsArray ? arrivalsArray.map((arrivals, index) => {
                return <Arrivals key={index} arrivals={arrivals} />
            }) : null}
        </div>
    )
}

export default LiveArrivals
