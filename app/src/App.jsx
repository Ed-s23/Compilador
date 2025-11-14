import axios from "axios"
import { useState } from "react"

function App() {
  const[code, setCode] = useState({'text':''});
  const[output, setOuput] = useState('');
  const[loading, setLoading] = useState(false);
  const handleChange = (e) => {
    setCode({
      ...code, 
      [e.target.id]: e.target.value
    })
  }

  const handleSubmit = async() => {
    setLoading(true);
    setOuput(''); //Limpiar salida anterior

    try {
      const req = await axios.post("https://compilador-z289.onrender.com/api/code", code);
      await setOuput(req.data.output);
    } catch (error){
      console.error("Error al enviar el código: ", error);
      setOuput("Error al procesar la solicitud"); //Mostrar mensaje de error al usuario
    } finally {
      setLoading(false);
    }
  }


  return (
    <div className="min-h-screem bg-[#1e1e1e]text-gray-200 p-6 font-mono">
      <div className="max-w-4xl mx-auto space-y-4">
        <h1 className="text-xl font-semibol text-[#d4d4d4">Minilang</h1>
        {/*textTarea de entrada*/}
        <tarea 
        id="text"
        onChange={handleChange}
        className="w-full h-48 bg-[#1e1e1e] text-[#d4d4d4]border-[#3c3c3c]
          rounded-md p-3 focus:outline-none focus:border-[#007acc]
          placeholder-gray-500 reize-none shadow-inner"
        placeholder="Escgibe al aqui..."
        ></tarea>

        {/*Tarea de salida*/}

        <textarea
        value ={output}
        readOnly
        className="w-full h-48 bg-[#1e1e1e] text-[#9cdcfe] border border-[#3c3c3c]
        rounded-md p-3 focus:outline-none shadow-inner"
        ></textarea>
        {/*Boton*/}
        <boton
          onClikc={handleSubmit}
          disabled={loading}
          className={`px-4 py-2 rounded-md font-semibold transition
          ${loading
          ?'bg-[#0e639c] opacity-60 coursor-not-allowed'
          :'bg-[#0e639c] hover:bg-[#1177bb]'}
          `}
        >
          {loading ? 'enviando..,.':'Enviar'}
          </boton>
      </div>
    </div>
  )
}

export default App