#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Fox :
		public Animal
	{
	public:
		Fox(World & world, const Point & position);
		virtual ~Fox() = default;

		void action() override;
	protected:
		inline const char * getSymbol() const override { return "FX"; }
		inline Kind getKind() const override { return Kind::Fox; }
	private:

	};

} // namespace bots
