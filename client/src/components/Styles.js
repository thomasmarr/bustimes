import styled from 'styled-components'
import { Link } from 'react-router-dom'

//Form Styles

export const InputField = styled.div`
    label {
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:focus + label {
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:focus {
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
    input[type=number].valid {
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
    input[type=number].invalid {
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
    -webkit-appearance: none; 
    margin: 0; 
    }
    .prefix.active {
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:not(.browser-default):focus:not([readonly])+label{
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:not(.broswer-default):focus:not([readonly]){
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
`

export const Input = styled.input`
    color:${props => props.theme.primaryFontColor};
`

export const Button = styled.button`
    &&& {
        background-color: ${props => props.theme.btnColor};
    }
`

export const DataWrapper = styled.div`
    margin: auto;
    font-family: '${props => props.theme.dataFont}', Arial, sans-serif;
    font-size: 28px;
    color: ${props => props.theme.dataFontColor};
    background-color: ${props => props.theme.dataBgColor};
    max-width:650px;
    margin-bottom: 20px;
`

export const LineWrapper = styled.div`
    grid-template-columns: 0.5fr 4fr 1fr;
    display: grid;
`

export const DataLeft = styled.div`
    margin: 0 0 0 10px;
    min-width:45px;
`
export const DataMiddle = styled.div`
    margin: 0 15px 0 15px;
    white-space: nowrap;
    overflow-x: scroll;
    height: 45px;
    ::-webkit-scrollbar {
        display: none;
    }
`
export const DataRight = styled.div`
    margin: 0 10px 0 0;
    overflow-x: hidden;
    white-space: nowrap;
    overflow-x: scroll;
    min-width:50px;
    ::-webkit-scrollbar {
        display: none;
    }
`

export const Header = styled.h4`
    color:${props => props.theme.headerFontColor};
    ext-align:center;
`

export const SubtlePara = styled.p`
    color:${props => props.theme.subtleFontColor};
`

export const SubtleLink = styled(Link)`
    &&& {
        color:${props => props.theme.subtleLinkFontColor};
    }
`