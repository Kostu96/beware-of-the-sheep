#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Antelope :
		public Animal
	{
	public:
		Antelope(World & world, const Point & position);
		virtual ~Antelope() = default;

		void action() override;
		void collision(Entity & other) override;
	protected:
		inline std::string getSymbol() const override { return "AT"; }
		inline Kind getKind() const override { return Kind::Antelope; }
		inline std::string getClassName() const override { return "Antelope"; }
	private:

	};

} // namespace bots
