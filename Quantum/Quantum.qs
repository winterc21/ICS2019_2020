
namespace ICS.Quantum{
	open Microsoft.Quantum.Intrinsic;
	open Microsoft.Quantum.Canon;
	open Microsoft.Quantum.Math;
	open Microsoft.Quantum.Diagnostics;
	open Microsoft.Quantum.Measurment;
	open Microsoft.Quantum.Samples;
	
	operation HelloWorld(): Unit{
		Message("Hello, World!");
	
	}
	
	operation Hello(name: String): Unit{
		Message($"Hello, {name}"); 
	}
	operation HelloSeward(): Unit{
		Hello("Mr. Seward");
	}
	operation QubitPlay() : Unit{
		using (q = Qubit()){
			x(q);
			if(M(q)==Zero){
				Message("It was Zero!");
			} else {
				Message("It was One!");
			}
			//elif
			Reset(q);
		}
	}		
}
