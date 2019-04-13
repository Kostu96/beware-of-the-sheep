#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Sheep :
		public Animal
	{
	public:
		Sheep(World & world, const Point & position);
		virtual ~Sheep() = default;
	protected:
		inline std::string getSymbol() const override { return "SP"; }
		inline Kind getKind() const override { return Kind::Sheep; }
		inline std::string getClassName() const override { return "Sheep"; }
	private:

	};

} // namespace bots
